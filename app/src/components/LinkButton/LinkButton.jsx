import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'

import './LinkButton.css';

import Navbar from '../Navbar/Navbar';

class LinkButton extends Component {
  render() {
    return (
        <div className="Parent"> 
          <a  className = "LinkButton" href="https://github.com/Roshanjossey/first-contributions/blob/master/README.md">
            <span> Get started </span>
          </a> 
          <a  className = "LinkButton">
            <span> Add a project </span>
          </a> 
        </div>   
    );
  }
}

export default LinkButton;
