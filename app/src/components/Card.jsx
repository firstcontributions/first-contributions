import React from 'react';
import './Card.css';

const Card = (props) => (
    <div className="CardContainer" >
        <div className="Row">
            <h1 className="CardTitle">{props.Info.title}</h1>
            <img className="Image" src={props.Info.src}/>
        </div>
        <p className="CardSummary">{props.Info.summary}</p>
        <a href={props.Info.site} className="CardLink">{props.Info.link}</a>
    </div>
);

export default Card;