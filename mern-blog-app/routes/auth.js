const express = require('express');
const passport = require('passport');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const router = express.Router();

// User registration route
router.post('/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = new User({ username, email, password: hashedPassword });
    await newUser.save();

    res.status(201).json({ message: 'User registered successfully' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// User login route
router.post('/login', (req, res, next) => {
  passport.authenticate('local', { session: false }, (err, user, info) => {
    if (err || !user) {
      return res.status(401).json({ message: 'Authentication failed' });
    }
    req.login(user, { session: false }, async (loginErr) => {
      if (loginErr) {
        return next(loginErr);
      }

      // Generate JWT tokens upon successful login
      const accessToken = jwt.sign({ _id: user._id }, 'your-secret-key', {
        expiresIn: '1h', // Adjust the expiration time as needed
      });
      const refreshToken = jwt.sign({ _id: user._id }, 'your-secret-key-refresh', {
        expiresIn: '7d', // Adjust the expiration time as needed
      });

      // Set tokens as cookies (you can also send them in the response body)
      res.cookie('accessToken', accessToken, { httpOnly: true });
      res.cookie('refreshToken', refreshToken, { httpOnly: true });

      return res.status(200).json({ message: 'Login successful' });
    });
  })(req, res, next);
});

// Logout route - Clear cookies
router.get('/logout', (req, res) => {
  res.clearCookie('accessToken');
  res.clearCookie('refreshToken');
  res.status(200).json({ message: 'Logout successful' });
});

module.exports = router;
