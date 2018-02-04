import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'
import Home from '../Home/Home';
import AddProject from '../AddProject/AddProject';




class Main extends Component {
  render() {
    return (
      <Switch>
          <Route exact path='/' component={Home}/>
          <Route path='/addProject' component={AddProject}/>
      </Switch>

    );
  }
}

export default Main;
