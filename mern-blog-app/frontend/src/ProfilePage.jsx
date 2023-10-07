import React, { useState } from 'react';

function ProfilePage() {
  const [editable, setEditable] = useState(false);
  const [userData, setUserData] = useState({
    username: 'User1',
    email: 'user@example.com',
    // Other user data
  });

  const handleEdit = () => {
    setEditable(true);
  };

  const handleSave = () => {
    // Send a PUT request to update user profile information
    setEditable(false);
  };

  const handleChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  return (
    <div>
      <h2>Your Profile</h2>
      {editable ? (
        <div>
          <button onClick={handleSave}>Save</button>
        </div>
      ) : (
        <div>
          <button onClick={handleEdit}>Edit</button>
        </div>
      )}
      <div>
        <label>Username:</label>
        <input
          type="text"
          name="username"
          value={userData.username}
          onChange={handleChange}
          readOnly={!editable}
        />
      </div>
      <div>
        <label>Email:</label>
        <input
          type="text"
          name="email"
          value={userData.email}
          onChange={handleChange}
          readOnly={!editable}
        />
      </div>
      {/* Other user data fields */}
    </div>
  );
}

export default ProfilePage;
