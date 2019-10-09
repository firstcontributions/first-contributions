import React, {Component} from 'react'
import {Link} from 'react-router-dom'

class HeaderNavigation extends Component {
    render() {
        return (
            <header class="nav">
                <div class="flex-container flex-row pad-top-25">
                    <div class="logo">
                        <Link to = '/'>
                            <a href="index.html">
                                <img src={require('../../assets/images/gojek-logo_normal.svg')} alt="Gojek Logo" />
                            </a>
                        </Link>
                    </div>
                    <div class="item-header flex-container flex-between">
                        <ul>
                            <li>
                                <Link to = '/about'>
                                    <a href="about.html">About Us</a>
                                </Link>
                            </li>
                            <li><a href="#Services">Services</a></li>
                            <li><a href="#Blog">Blog</a></li>
                            <li><a href="#HelpCentre">Help Centre</a></li>
                            <li><a href="#JoinUs">Join Us</a></li>
                            <li>
                                <Link to = '/cerdikiawan'>
                                    <a href="cerdikiawan.html">Cerdikiawan</a>
                                </Link>
                            </li>
                        </ul>
                    </div>
                    <div class="language">
                        <a href="#language">English</a>
                    </div>
                </div>
            </header>
        )
    }
}

export default HeaderNavigation