import React from 'react';
import TwitterCard from './Twitter';
import FacebookCard from './Facebook';
import GoogleCard from './Google';
import './SocialShare.css';

const SocialShare = () => (
    <section id='social-share'>
        <h2>Share the news of your first contribution</h2>
        <div id='social-shares-container'>
            <TwitterCard/>
            <FacebookCard/>
            <GoogleCard/>
        </div>
    </section>
);

export default SocialShare
