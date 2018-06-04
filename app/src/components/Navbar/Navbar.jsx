import React, { Component } from 'react';
import './Navbar.css';

class Navbar extends Component {
    render() {
        return (
            <div className="topnav">
                <a href="https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY"  target="_blank" rel="noopener noreferrer">Slack</a>
                <a href="https://twitter.com/1stContribution" target="_blank" rel="noopener noreferrer">Twitter</a>
                <a href="https://github.com/Roshanjossey/first-contributions" target="_blank" rel="noopener noreferrer">GitHub</a>
            </div>
        );
    }
}

export default Navbar;
