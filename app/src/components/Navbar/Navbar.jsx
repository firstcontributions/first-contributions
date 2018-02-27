import React, { Component } from 'react';
import './Navbar.css';

class Navbar extends Component {
    render() {
        return (
            <div className="topnav">
                <a href="https://firstcontributions.herokuapp.com"  target="_blank" rel="noopener noreferrer">Slack</a>
                <a href="https://twitter.com/1stContribution" target="_blank" rel="noopener noreferrer">Twitter</a>
                <a href="https://github.com/Roshanjossey/first-contributions" target="_blank" rel="noopener noreferrer">GitHub</a>
            </div>
        );
    }
}

export default Navbar;
