// BlogList.jsx
import React, { useEffect, useState } from 'react';

function BlogList() {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    // Fetch the user's blogs from the backend
  }, []);

  return (
    <div>
      <h2>Your Blogs</h2>
      <ul>
        {blogs.map((blog) => (
          <li key={blog._id}>
            {blog.title} - {blog.content}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BlogList;
