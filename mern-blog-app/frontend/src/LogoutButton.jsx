import React from 'react';

function LogoutButton() {
  const handleLogout = () => {
    // Clear authentication tokens and log the user out
    // Remove the authentication tokens from client-side storage (e.g., localStorage)
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');

    // Redirect the user to the login page or perform any other necessary actions
    // You can use React Router to navigate to the login page
    // Example: history.push('/login');
  };

  return <button onClick={handleLogout}>Logout</button>;
}

export default LogoutButton;
