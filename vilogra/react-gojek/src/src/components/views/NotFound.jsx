import React, { Component } from 'react'
import {Link} from 'react-router-dom'
import '../.././NotFound.scss'

export default class NotFound extends Component {
    render() {
        return (
            <div id="notfound">
                <div class="notfound">
                    <div class="notfound-404">
                        <h1>Oops!</h1>
                        <h2>404 - The Page can't be found</h2>
                    </div>
                    <Link to = '/'>
                        <a href="#">Go TO Homepage</a>
                    </Link>
                </div>
            </div>
        )
    }
}
