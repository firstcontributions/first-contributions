const express = require('express');
const passport = require('passport');
const cookieParser = require('cookie-parser');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const User = require('./models/User'); // Import the User model

const app = express();
app.use(express.json());
app.use(cookieParser());

// Passport.js configuration (passport-config.js) - Same as before

// Middleware to protect routes
function authenticateUser(req, res, next) {
  passport.authenticate('jwt', { session: false }, (err, user) => {
    if (err || !user) {
      return res.status(401).json({ message: 'Unauthorized' });
    }
    req.user = user;
    return next();
  })(req, res, next);
}

// Register a new user
app.post('/register', async (req, res) => {
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

// Login route
app.post('/login', (req, res, next) => {
  passport.authenticate('local', { session: false }, (err, user, info) => {
    if (err || !user) {
      return res.status(401).json({ message: 'Authentication failed' });
    }
    req.login(user, { session: false }, (loginErr) => {
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

// Protected route example - User homepage
app.get('/user-homepage', authenticateUser, (req, res) => {
  // Fetch and send user's blogs to the frontend
  res.status(200).json({ message: 'User homepage data' });
});

// Extend the backend to handle user-specific blog operations (create, edit, delete)

// Logout route - Clear cookies
app.get('/logout', (req, res) => {
  res.clearCookie('accessToken');
  res.clearCookie('refreshToken');
  res.status(200).json({ message: 'Logout successful' });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
