const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  blogs: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Blog' }], // Array of Blog ObjectIds by a user
  // Add more fields as needed
});

module.exports = mongoose.model('User', userSchema);
