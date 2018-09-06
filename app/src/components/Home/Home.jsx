import React, { Component } from 'react';
import CardsContainer from '../ProjectList/CardsContainer';
import SocialShare from '../SocialShare/SocialShare';
import LinkButton from '../LinkButton/LinkButton';


class Home extends Component {
  render() {
    return (
    <home>
      <LinkButton />
      <CardsContainer/>
      <SocialShare/>
    </home>

    );
  }
}

export default Home;
