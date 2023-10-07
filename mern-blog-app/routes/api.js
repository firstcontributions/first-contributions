const express = require('express');
const router = express.Router();
const Blog = require('../models/Blog.js');
const User = require('../models/User');
const Comment = require('../models/Comment');

// Create a new blog post
router.post('/blogs', async (req, res) => {
  try {
    const { title, content, authorId } = req.body;
    const author = await User.findById(authorId);

    if (!author) {
      return res.status(404).json({ error: 'User not found' });
    }

    const newBlog = new Blog({ title, content, author: authorId });
    await newBlog.save();

    author.blogs.push(newBlog);
    await author.save();

    res.json(newBlog);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Retrieve all blog posts
router.get('/blogs', async (req, res) => {
  try {
    const blogs = await Blog.find().populate('author').populate('comments');
    res.json(blogs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Retrieve a single blog post by ID
router.get('/blogs/:id', async (req, res) => {
  try {
    const blog = await Blog.findById(req.params.id).populate('author').populate('comments');
    if (!blog) {
      return res.status(404).json({ error: 'Blog not found' });
    }
    res.json(blog);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a blog post by ID
router.put('/blogs/:id', async (req, res) => {
  try {
    const { title, content } = req.body;
    const updatedBlog = await Blog.findByIdAndUpdate(
      req.params.id,
      { title, content },
      { new: true }
    ).populate('author').populate('comments');
    if (!updatedBlog) {
      return res.status(404).json({ error: 'Blog not found' });
    }
    res.json(updatedBlog);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete a blog post by ID
router.delete('/blogs/:id', async (req, res) => {
  try {
    const deletedBlog = await Blog.findByIdAndRemove(req.params.id).populate('author');
    if (!deletedBlog) {
      return res.status(404).json({ error: 'Blog not found' });
    }

    const author = await User.findById(deletedBlog.author);
    if (author) {
      author.blogs.pull(deletedBlog);
      await author.save();
    }

    res.json(deletedBlog);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
