import React from 'react';
import './Card.css';

/**
 * This is the card component. It is done in a stateless component manner. An JS object
 * is passed in via props to populate the card with information. The styling for this 
 * component is found in Card.CSS
 * @param {*} props 
 */
const Card = (props) => (
    <div className="CardContainer" >
        <div className="Row">
            <h1 className="CardTitle">{props.Info.title}</h1>
            <img className="Image" src={props.Info.src}/>
        </div>
        <p className="CardSummary">{props.Info.summary}</p>
        <a href={props.Info.site} className="CardLink">View Project</a>
    </div>
);

export default Card;