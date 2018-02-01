import React, { Component } from 'react';
import './LinkButton.css';

class LinkButton extends Component {
  render() {
    return (
      <a className="LinkButton" href="https://github.com/Roshanjossey/first-contributions/blob/master/README.md">
        <span> Get started </span>
      </a>
    );
  }
}

export default LinkButton;
