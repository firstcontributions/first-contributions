import React, { Component } from 'react'
import Cover from '../../assets/images/HOME-PAGE.jpg'

export default class CerdikiawanContent extends Component {
    render() {
        return (
            <div>
                <div class="section home margin-bot-10">
                    <div class="container-fluid cover" style={backgroundCover}>
                        <div class="container">
                            <h1>Gojek Proudly <span>Presents</span> <span>CERDIKIAWAN</span> <span>AWARDS</span></h1>
                            <p>#ThereIsAlwaysAWay</p>
                            <button type="submit">See Video</button>
                        </div>
                    </div>
                </div>

                <div class="section about-cerdikiawan">
                    <div class="flex-container margin-bot-4">
                        <h3>About Cerdikiawan</h3>
                    </div>
                    <div class="container-fluid margin-bot-10">
                        <div class="container">
                            <div class="row">
                                <div class="col-6">
                                    <img src={require("../../assets/images/cerdikiawan_1.jpg")} alt="Gojek Cerdikiawan" />
                                </div>
                                <div class="col-6 centering">
                                    <div class="text">
                                        <h3>A Clever Flock of the Nation's Children</h3>
                                        <p>A cerdikiawan is a clever Indonesian with copious tricks up their sleeves. They bring out the best of themselves to outsmart every problem.</p>
                                        <p>Nothing can stop them because a Cerdikiawan always finds a way to hack through any situation.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="container-fluid margin-bot-10">
                        <div class="container">
                            <div class="row">
                                <div class="col-6 centering">
                                    <div class="textr">
                                        <h3>#ThereIsAlwaysAWay</h3>
                                        <p>The spirit of Cerdikiawan is reflected in Gojek, which was originally formed to hack traffic jams and problems.</p>
                                        <p>Now Gojek provides more than 20 services to help you hack your daily challenges.</p>
                                        <p>Should you arrive at the office early? GoCar got you covered. Your first day in the new office? Order GoFood to make new friends.</p>
                                        <p>Whatever the problem, #PastiAdaJalan with Gojek.</p>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <img src={require("../../assets/images/cerdikiawan_2.jpg")} alt="Gojek Cerdikiawan" />
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="container-fluid margin-bot-10">
                        <div class="container">
                            <div class="row">
                                <div class="col-6">
                                    <img src={require("../../assets/images/cerdikiawan_3.jpg")} alt="Gojek Cerdikiawan" />
                                </div>
                                <div class="col-6 centering">
                                    <div class="text">
                                        <h3>Be a Cerdikiawan</h3>
                                        <p>Let’s be a part of Cerdikiawan with Gojek!</p>
                                        <p>Do you have any unique innovations to hack or outsmart your daily problems? If yes, stay tune! Because something exciting is coming along with great prizes.</p>                                
                                        <p>Keep your eyes on this page, and be the first to join and win.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="flex-container margin-bot-10">
                        <div class="container">
                            <a href="#"><img src={require("../../assets/images/2111f4a6b75a0b280239cb0f917d7630.webp")} alt="Gojek Cerdikiawan" /></a>
                        </div>
                    </div>
                    <div class="container-fluid margin-bot-10">
                        <div class="container">
                            <div class="row">
                                <div class="col-6 centering">
                                    <div class="textr">
                                        <h3>Show your smart innovation!</h3>
                                        <p>Take a picture of your smart innovation using the Cerdikiawan Instagram filter from @gojekindonesia and upload it to your social media. Don’t forget to tag us!</p>
                                        <button type="submit" class="btn-1">T&C</button>
                                        <button type="submit" class="btn-2">Submit Now</button>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <img src={require("../../assets/images/cerdikiawan_4.jpg")} alt="Gojek Cerdikiawan" />
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="container-fluid margin-bot-10">
                        <a href="#"><img src={require("../../assets/images/cerdikiawan-banner.png")} alt="Gojek Cerdikiawan" /></a>
                    </div>
                    <div class="flex-container margin-bot-10">
                        <div class="container">
                            <a href="#"><img src={require("../../assets/images/36d79ea90fc511114effdd6410c85fdd.webp")} alt="Gojek Cerdikiawan" /></a>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

const backgroundCover = {
    backgroundImage: `url(${Cover})`
}