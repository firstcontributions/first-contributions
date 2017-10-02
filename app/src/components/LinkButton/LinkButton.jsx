import React, { Component } from 'react';
import './LinkButton.css';

class LinkButton extends Component {
  render() {
    return (
		<a className="twitter-share-button"
		href="https://twitter.com/intent/tweet?text=Hello%20world">
		Tweet</a>
    );
  }
}

export default LinkButton;
