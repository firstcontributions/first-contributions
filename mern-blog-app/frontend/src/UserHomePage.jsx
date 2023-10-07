import React, { useState, useEffect } from 'react';
import BlogForm from './BlogForm';

function UserHomePage() {
  const [blogs, setBlogs] = useState([]);
  const [editingBlog, setEditingBlog] = useState(null);

  useEffect(() => {
    // Fetch user's blogs from the backend and set them in the 'blogs' state
  }, []);

  const handleEdit = (blog) => {
    setEditingBlog(blog);
  };

  const handleCancelEdit = () => {
    setEditingBlog(null);
  };

  return (
    <div>
      <h2>Your Blogs</h2>
      <button onClick={() => setEditingBlog({})}>Create New Blog</button>
      <ul>
        {blogs.map((blog) => (
          <li key={blog._id}>
            {blog.title} - {blog.content}
            <button onClick={() => handleEdit(blog)}>Edit</button>
          </li>
        ))}
      </ul>
      {editingBlog && (
        <BlogForm
          blog={editingBlog}
          onCancel={handleCancelEdit}
          onSuccess={() => {
            // Fetch updated list of blogs after creating/editing a blog
            // Reset 'editingBlog' state to null
          }}
        />
      )}
    </div>
  );
}

export default UserHomePage;
