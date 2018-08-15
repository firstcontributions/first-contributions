import React from 'react';
import './css/project-cards.css';

export default class Card extends React.Component {
  render() {
    let tags = [];
    if (this.props.tags){
        tags = this.props.tags.map((tag, key) => <div key={key}><p>{tag}</p></div>)
    }

    return (
      <div className="Card-Container">
        <a  className="Card-Real-Link" href={this.props.githubLink}>
          <div className="Card-Header">
            <img className="Project-Logo"
              alt="the framework or language that the project is build upon"
              src={this.props.logoLink} />
            <h3 className="Card-Title">{ this.props.name }</h3>
          </div>
          <div className="Card-Body">
            <div className="Card-Tag">
                {tags}
            </div>
            <div className="Card-Description">
              <p> { this.props.description }</p>
            </div>
            <div className="Card-Link">
              Go to Project
            </div>
          </div>
        </a>
      </div>
    );
  }
}
