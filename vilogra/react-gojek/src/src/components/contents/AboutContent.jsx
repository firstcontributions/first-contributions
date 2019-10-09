import React, { Component } from 'react'

export default class AboutContent extends Component {
    render() {
        return (
            <div>
                <div class="section welcome margin-bot-14">
                    <div class="flex-container">
                        <div class="title-welcome">
                            <h3>Welcoming a fresh start</h3>
                        </div>
                    </div>
                    <div class="container-fluid">
                        <div class="container">
                            <div class="row">
                                <div class="col-8">
                                    <p>Meet Solv, Gojek’s new logo</p><br />
                                    <p>Founded on the principle of solving everyday challenges with technology, the Gojek app has evolved from offering just ride-hailing to a suite of more than 20 services today. As we continue to grow as a leading tech company serving everyday solutions for millions of users across Southeast Asia, our passion for problem-solving grows.</p><br />
                                            
                                    <p>This journey builds on our ever-present dedication to creating seamless experiences for users, and providing the socio-economy impact for millions of our partners (drivers, merchants, service providers).</p><br />
                                         
                                    <p>Our new logo symbolizes Gojek’s transformation from being a ride-hailing service to becoming the largest Super App with three platforms: consumer, driver, and merchant applications, with a variety of smart ways to eliminate hassles.</p><br />
                                            
                                    <p>We believe that with Gojek, and with continuous technological innovations, There Is Always A Way to solve everyday problems and affect positive social impact.</p>
                                </div>
                                <div class="col-3 pad-left95">
                                    <img src={require("../../assets/images/about_1.jpg")} alt="Gojek About"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="section history margin-bot-14">
                    <div class="container-fluid">
                        <div class="container">
                            <div class="row">
                                <div class="col-3 centering">
                                    <img src={require("../../assets/images/about_2.jpg")} alt="Gojek About"/>
                                </div>
                                <div class="col-8 pad-left95">
                                    <h3>History</h3>
                                    <p>Gojek’s journey began in 2010 as a motorcycle ride-hailing call center in Indonesia. The homegrown app was then launched in 2015 with only three services: GoRide, GoSend, and GoMart.</p><br/>
                                    <p>Since then, the app has evolved into a Super App, a multi-services platform with more than 20 services today.</p><br/>
                                    <p>Gojek is now a leading technology group of platform serving millions of users in Southeast Asia.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="section pillars margin-bot-14">
                    <div class="flex-container centering margin-bot-4">
                        <h3>The 3 Gojek Pillars</h3>
                    </div>
                    <div class="flex-container" style={aboutStyle}>
                        <div class="item-pillars">
                            <img src={require("../../assets/images/speed.svg")} alt="Gojek Pillars"/>
                            <h4>Speed</h4>
                            <p>Our service is fast, and we continually learn and grow from experience.</p>
                        </div>
                        <div class="item-pillars">
                            <img src={require("../../assets/images/innovation.svg")} alt="Gojek Pillars"/>
                            <h4>Innovation</h4>
                            <p>We work hard to continuously improve our services, so that they provide more ease for users.</p>
                        </div>
                        <div class="item-pillars">
                            <img src={require("../../assets/images/social-impact.svg")} alt="Gojek Pillars"/>
                            <h4>Social Impact</h4>
                            <p>We work to create as much positive social impact as possible for Gojek users.</p>
                        </div>
                    </div>
                </div>

                <div class="section about-services margin-bot-14">
                    <div class="container-fluid">
                        <div class="container">
                            <div class="row">
                                <div class="col-6">
                                    <img src={require("../../assets/images/about_3.jpg")} alt="Gojek About"/>
                                </div>
                                <div class="col-6 centering">
                                    <div class="text">
                                        <h3>Services</h3>
                                        <p>Through just one platform, Gojek’s users can access over 20 services ranging from transportation to food delivery, massages, e-money, and even a loyalty program. Because with Gojek, There Is Always A Way.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="section social-economy margin-bot-14">
                    <div class="container-fluid">
                        <div class="container">
                            <div class="row">
                                <div class="col-6 centering">
                                    <div class="text">
                                        <h3>Social Economy Impact</h3><br />
                                        <p>Research by the Demographic Institute of the Faculty of Economics & Business, University of Indonesia, in 2018, involving 6,732 respondents, conducted across 9 cities in Indonesia.</p><br />
                                        <p><strong>Delivering Economic Impact For Indonesia</strong></p>
                                        <p>Gojek contributed around <strong>Rp44.2 trillion (US$3 billion) to the Indonesian</strong> economy as of end 2018*.</p><br />
                                        <p><strong>Our Impact Helps The Members In Our Ecosystem Driver-partners</strong></p>
                                        <p>After joining Gojek, the quality of life of our <strong>driver-partners’ have increased—100%</strong> of them believe that they can provide better well-being for their family. Most also claim they can now send their children to school, especially with the fair incentives and policies that Gojek provides.</p><br />
                                        <p><strong>Merchants</strong></p>
                                        <p>Gojek’s ecosystem supports <strong>the growth of MSMEs in Indonesia. 93%</strong> of MSME partners experience an increase in transaction volume and <strong>55%</strong> of them experience an increase in earnings.</p><br />
                                        <p><strong>Service providers</strong></p>
                                        <p><strong>GoLife partners with more than 60,000 service providers, 70%</strong> of which are female; and <strong>90%</strong>s are high school graduates. Approximately 1 in 20 of our GoLife service providers in GoMassage and GoAuto are persons with disabilities.</p>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <img src={require("../../assets/images/about_4.jpg")} alt="Gojek About"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="section awards margin-bot-14">
                    <div class="flex-container centering margin-bot-4">
                        <h3>Awards</h3>
                    </div>
                    <div class="flex-container">
                        <div class="container">
                            <img src={require("../../assets/images/about_banner.png")} alt="Gojek Awards"/>
                        </div>
                    </div>
                </div>

                <div class="section channels margin-bot-14">
                    <div class="flex-container centering margin-bot-4">
                        <h3>Official Channels</h3>
                    </div>
                    <div class="container-fluid">
                        <div class="container">
                            <div class="row">
                                <div class="col-4">
                                    <div class="text">
                                        {/* <!-- Gojek Indonesia --> */}
                                        <h3>Gojek <span>Indonesia</span></h3>
                                        <p>@gojekindonesia</p>
                                        <p>Gojek Indonesia</p>
                                        <p>@gojekindonesia</p>
                                        <p>Gojek Indonesia</p>
                                        <p>Gojek Indonesia</p><br/><hr/><br/>
                                        {/* <!-- Go Box --> */}
                                        <h3>GoBox</h3>
                                        <p>@goboxindonesia</p><br/><hr/><br/>
                                        {/* <!-- Go Send--> */}
                                        <h3>GoSend</h3>
                                        <p>@gosendindonesia</p><br/><hr/><br/>
                                         {/* <!-- Gojek Promo--> */}
                                        <h3>Gojek Promo</h3>
                                        <p>@gojekpromo</p>
                                        <p>@gojekpromo</p><br/><hr/><br/>
                                         {/* <!-- GoPay --> */}
                                        <h3>GoPay</h3>
                                        <p>@gopayindonesia</p>
                                        <p>@gopayindonesia</p>
                                        <p>GoPay Indonesia</p>
                                        <p>Gopay Indonesia</p><br/><hr/><br/>
                                        {/* <!-- GoFood--> */}
                                        <h3>GoFood</h3>
                                        <p>@gofoodindonesia</p><br/><hr/>
                                    </div>
                                </div>
                                <div class="col-4">
                                    <div class="text">
                                        {/* <!-- GoPoints --> */}
                                        <h3>GoPoints</h3>
                                        <p>@gopointsindonesia</p><br/><hr/><br/>
                                        {/* <!-- GoTix --> */}
                                        <h3>GoTix</h3>
                                        <p>@gotixindonesia</p>
                                        <p>@gotixindonesia</p>
                                        <p>GoTix Indonesia</p>
                                        <p>GoTix Indonesia</p><br/><hr/><br/>
                                        {/* <!-- GoLife --> */}
                                        <h3>GoLife</h3>
                                        <p>@golifeindonesia</p>
                                        <p>@golifeindonesia</p>
                                        <p>GoLife Indonesia</p>
                                        <p>GoLife Indonesia</p><br/><hr/><br/>
                                        {/* <!-- GO-VIET (Vietnam) --> */}
                                        <h3>GO-VIET (Vietnam)</h3>
                                        <p>Facebook (driver page)</p>
                                        <p>GO-VIET fanpage</p>
                                        <p>GO-FOOD fanpage</p>
                                        <p>GO-VIET YouTube page</p>
                                        <p>GO-FOOD YouTube page</p>
                                        <p>GO-VIET Instagram</p>
                                        <p>GO-FOOD Instagram</p><br/><hr/><br/>
                                        {/* <!-- Gojek Singapore --> */}
                                        <h3>Gojek Singapore</h3>
                                        <p>Facebook</p>
                                        <p>Instagram</p>
                                        <p>Twitter</p>
                                        <p>Website</p><br/><hr/><br/>
                                    </div>
                                </div>
                                <div class="col-4">
                                    <div class="text">
                                        {/* <!-- GET! (Thailand) --> */}
                                        <h3>GET! (Thailand)</h3>
                                        <p>Facebook (user page)</p>
                                        <p>Facebook (driver page)</p>
                                        <p>LinkedIn</p>
                                        <p>Twitter</p><br/><hr/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

const aboutStyle = {
    alignItems: 'center',
    justifyContent: 'spaceBetween'
}