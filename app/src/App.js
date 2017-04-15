import React, { Component } from 'react';
import './App.css';
import LinkButton from './components/LinkButton';
import Card from './components/Card';

const ReactOS = {
  title: "React",
  summary: "Javascript library for redering UI",
  link: "Github page",
  site: "https://facebook.github.io/react/",
  src: "https://s3.amazonaws.com/media-p.slid.es/uploads/espenhovlandsdal/images/566501/react-logo-colored.png"
};

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
        <Card Info={ReactOS}/>
      </div>
    );
  }
}

export default App;
