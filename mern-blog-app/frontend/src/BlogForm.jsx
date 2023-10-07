// BlogForm.jsx
import React, { useState } from 'react';

function BlogForm() {
  const [formData, setFormData] = useState({
    title: '',
    content: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Send a POST request to create or update the blog
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="title"
        placeholder="Blog Title"
        value={formData.title}
        onChange={handleChange}
      />
      <textarea
        name="content"
        placeholder="Blog Content"
        value={formData.content}
        onChange={handleChange}
      />
      <button type="submit">Save Blog</button>
    </form>
  );
}

export default BlogForm;
