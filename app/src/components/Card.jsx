import React from 'react';
import './Card.css';

const Card = (props) => (
    <div className="CardContainer" >
        <h1 className="CardTitle">{props.Info.title}</h1>
        <p className="CardSummary">{props.Info.summary}</p>
        <a href={props.Info.site} className="CardLink">{props.Info.link}</a>
    </div>
);

export default Card;