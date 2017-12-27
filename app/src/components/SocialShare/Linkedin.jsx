import React from 'react';
import { Icon, IconPaths } from './icons.js';

const LinkedinCard = "https://www.linkedin.com/shareArticle?mini=true&url=https://roshanjossey.github.io/first-contributions/#social-share&title=LinkedIn%20First%Contributions&hashtags=OpenSource,CodeNewbie"

const LinkedinCard = () => (
    <a className="icon-card linkedin" href={LinkedinLink} target="_blank">
        <Icon
            color="rgb(255, 255, 255)"
            size={40}
            icon={IconPaths.linkedin}
        />
    </a>
);

export default LinkedinCard;
