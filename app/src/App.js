import React, { Component } from 'react';
import './App.css';
// import LinkButton from './components/LinkButton/LinkButton';
// import Navbar from './components/Navbar/Navbar';
//import Search from './components/Search/Search';
import CardsContainer from './components/ProjectList/ContainerForCards';
class App extends Component {
  render() {
    return (
      <div className="App">
      
      <CardsContainer/>
      </div>
    );
  }
}

export default App;
