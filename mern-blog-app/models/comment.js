const mongoose = require('mongoose');

const commentSchema = new mongoose.Schema({
  text: String,
  author: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }, // Comment author schema ObjectId
  // Add more fields as needed
});

module.exports = mongoose.model('Comment', commentSchema);
