const mongoose = require('mongoose');

const blogSchema = new mongoose.Schema({
  title: String,
  content: String,
  author: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }, // Blog author schema ObjectId
  comments: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Comment' }], // Array of Comment ObjectIds
  // Add more fields as needed
});

module.exports = mongoose.model('Blog', blogSchema);
