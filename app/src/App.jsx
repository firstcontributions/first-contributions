import React, { Component } from 'react';
import './App.css';
import Navbar from './components/Navbar/Navbar';
import Main from './components/Main/Main';



class App extends Component {
    render() {
        return (
            <div className="App">
                <Navbar />
                <Main/>
                {/* <div className="App-header">
                    <h1>Make your first open source contribution in 5 minutes</h1>
                </div>
                <LinkButton />
                <CardsContainer />
                <SocialShare/> */}
            </div>
        );
    }
}

export default App;
