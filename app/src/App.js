import React, { Component } from 'react';
import './App.css';
import LinkButton from './components/LinkButton';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
        <h1>Make your first open source contribution in 5 minutes</h1>
        </div>
      <LinkButton />
      </div>
    );
  }
}

export default App;
