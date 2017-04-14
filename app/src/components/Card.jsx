import React from 'react';
import './Card.css';

const Card = (props) => (
    <div className="CardContainer" >
        <h1 className="CardTitle">{props.title}</h1>
        <p className="CardSummary">{props.summary}</p>
        <a className="CardLink">{props.link}</a>
    </div>
);

export default Card;