import React from 'react';
import { Icon, IconPaths } from './icons.js';

const GoogleLink = "https://plus.google.com/share?url=https://roshanjossey.github.io/first-contributions&prefilltext=I have made my first PR using this tutorial and I find it really simple and encouraging."

const GoogleCard = () => (
    <a className="icon-card " href={GoogleLink} target="_blank">
        <Icon
            color="rgb(255, 255, 255)"
            size={50}
            icon={IconPaths.google}
            boxStyle="0 0 24 22"
        />
    </a>
);

export default GoogleCard;
