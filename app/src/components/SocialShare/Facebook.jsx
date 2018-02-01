import React from 'react';
import { Icon, IconPaths } from './icons.js';

const facebookLink = "https://www.facebook.com/sharer/sharer.php?u=https://roshanjossey.github.io/first-contributions&quote=Yay%21%20I%20just%20made%20my%20first%20open%20source%20contribution%20with%20First%20Contributions.%20You%20can%20too,%20by%20following%20a%20simple%20tutorial%20at%20https%3A//goo.gl/66Axwe"

const FacebookCard = () => (
    <a className="icon-card twitter" href={facebookLink} target="_blank">
        <Icon
            color="rgb(255, 255, 255)"
            size={40}
            icon={IconPaths.facebook}
            boxStyle="0 0 22 22"
        />
    </a>
);

export default FacebookCard;
