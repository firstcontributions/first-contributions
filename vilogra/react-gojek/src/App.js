import React, { Component } from 'react'
import "./App.css";
import { BrowserRouter as Router, Route, Switch as TPLink } from 'react-router-dom'
import HeaderNavigation from './components/views/HeaderNavigation'
import FooterNavigation from './components/views/FooterNavigation'
import HomeContent from './components/contents/HomeContent'
import AboutContent from './components/contents/AboutContent'
import CerdikiawanContent from './components/contents/CerdikiawanContent'
import NotFound from './components/views/NotFound'

class App extends Component {
  render() {
    return (
      <Router>
        <HeaderNavigation />
          <TPLink>
            <Route path = '/' exact component = {HomeContent}/>
            <Route path = '/about' component = {AboutContent}/>
            <Route path = '/cerdikiawan' component = {CerdikiawanContent}/>
            <Route component = {NotFound} />
          </TPLink>
        <FooterNavigation />
      </Router>
    )
  }
}

export default App