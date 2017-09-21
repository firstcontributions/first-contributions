import React from 'react';
import Search from '../Search/Search';
import './ContainerForCards.css';

export default class CardsContainer extends React.Component{

    render(){

        return(
            <div className="Container-layout">
                <Search/>
            </div>

        )
    }

}