import React from 'react';
import TwitterCard from './Twitter';
import FacebookCard from './Facebook';
import LinkedinCard from './Linkedin';
import './SocialShare.css';

const SocialShare = () => (
    <section id='social-share'>
        <h2>Share the news of your first contribution</h2>
        <div id='social-shares-container'>
            <TwitterCard/>
            <FacebookCard/>
            <LinkedinCard/>

        </div>
    </section>
);

export default SocialShare
