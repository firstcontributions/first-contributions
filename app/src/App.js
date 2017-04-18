import React, { Component } from 'react';
import './App.css';
import LinkButton from './components/LinkButton';
import Card from './components/Card';
import ProjectsList from './components/ProjectsList'; 

class App extends Component {
  render() {
    return (
      <div>
        <div className="App">
          <div className="App-header">
          <h1>Make your first open source contribution in 5 minutes</h1>
          </div>
          <LinkButton />
        </div>
        <ProjectsList />
      </div>
    );
  }
}

export default App;
