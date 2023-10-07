const express = require('express');
const router = express.Router();
const passport = require('passport');
const Blog = require('../models/Blog');
const User = require('../models/User');

// Middleware to protect routes - Require user authentication
function authenticateUser(req, res, next) {
  passport.authenticate('jwt', { session: false }, (err, user) => {
    if (err || !user) {
      return res.status(401).json({ message: 'Unauthorized' });
    }
    req.user = user;
    return next();
  })(req, res, next);
}

// User homepage route - Retrieve and send user's blogs
router.get('/user-homepage', authenticateUser, async (req, res) => {
  try {
    const user = req.user;
    // Fetch user's blogs and send them to the frontend
    const blogs = await Blog.find({ author: user._id }).populate('comments');
    res.status(200).json({ blogs });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Create a new blog route
router.post('/blogs', authenticateUser, async (req, res) => {
  try {
    const { title, content } = req.body;
    const author = req.user._id;

    const newBlog = new Blog({ title, content, author });
    await newBlog.save();

    // Add the new blog's ID to the user's blogs array
    const user = await User.findById(author);
    user.blogs.push(newBlog);
    await user.save();

    res.status(201).json({ message: 'Blog created successfully', blog: newBlog });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Update a blog route
router.put('/blogs/:id', authenticateUser, async (req, res) => {
  try {
    const { title, content } = req.body;
    const blogId = req.params.id;

    const updatedBlog = await Blog.findByIdAndUpdate(
      blogId,
      { title, content },
      { new: true }
    );

    if (!updatedBlog) {
      return res.status(404).json({ message: 'Blog not found' });
    }

    res.status(200).json({ message: 'Blog updated successfully', blog: updatedBlog });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Delete a blog route
router.delete('/blogs/:id', authenticateUser, async (req, res) => {
  try {
    const blogId = req.params.id;

    const deletedBlog = await Blog.findByIdAndRemove(blogId);

    if (!deletedBlog) {
      return res.status(404).json({ message: 'Blog not found' });
    }

    // Remove the blog's ID from the user's blogs array
    const user = req.user;
    user.blogs.pull(blogId);
    await user.save();

    res.status(200).json({ message: 'Blog deleted successfully', blog: deletedBlog });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
