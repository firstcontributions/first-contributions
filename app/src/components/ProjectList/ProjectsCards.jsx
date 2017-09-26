import React from 'react';
import './ProjectsCards.css';
export default class Card extends React.Component {
    render() {
        return (
            <a className="Card-Container" href={this.props.link}>
                <div className="Card-Header">
                    <h3 className="Card-Title">{this.props.name}</h3>
                    <img className="Project-Logo" alt="the framework or language that the project is build upon" src={this.props.logo}/>
                </div><div className="Card-Body">
                    <div className="Card-Description">
                        <p> {this.props.description}</p>
                    </div>  
                </div><div className="Card-Link">
                Link to Project
                </div>
            </a>
        )
    }
}