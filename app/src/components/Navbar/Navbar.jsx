import React, { Component } from 'react';
import './Navbar.css';

class Navbar extends Component {
  render() {
    return (
      <div className="topnav">
        <a href="https://github.com/Roshanjossey/first-contributions" target="_blank">GitHub</a>
        <a href="https://twitter.com/1stContribution" target="_blank">Twitter</a>
        <a href="https://firstcontributions.herokuapp.com"  target="_blank">Slack</a>
      </div>
    );
  }
}

export default Navbar;
