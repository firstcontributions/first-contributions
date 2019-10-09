import React, { Component } from 'react'
import Cover from '../../assets/images/HOME-PAGE.jpg'

export default class HomeContent extends Component {
    render() {
        return (
            <div>
                <div class="section home margin-bot-10">
                    <div class="container-fluid cover" style={backgroundCover}>
                        <div class="container">
                            <h1>Gojek Proudly <span>Presents</span> <span>CERDIKIAWAN</span></h1>
                            <p>#ThereIsAlwaysAWay</p>
                            <button type="submit">See Video</button>
                        </div>
                    </div>
                </div>

                <div class="section solv margin-bot-10">
                    <div class="container-fluid">
                        <div class="container">
                            <div class="row">
                                <div class="col-6">
                                    <img src={require("../../assets/images/solv-gojek.jpg")} alt="Super App"/>
                                </div>
                                <div class="col-6 centering">
                                    <div class="text">
                                        <h3>Meet Solv, Gojek's new logo</h3>
                                        <p>
                                            Our new logo symbolizes Gojek’s transformation from being a ride-hailing service to becoming the largest Super App, with a variety of smart ways to eliminate hassles.
                                        </p>
                                        <a href="#FindOut">Find Out Here</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="section slider margin-bot-10">
                    <div class="container-fluid">
                        <div class="container">
                            <img src={require("../../assets/images/991e329ebb01d68dfadf0dd606b4a4cb.webp")} alt="Banner Slider"/>
                        </div>
                    </div>
                </div>

                <div class="section services margin-bot-10">
                    <div class="flex-container text">
                        <h3>Our Services</h3>
                    </div>
                    <div class="flex-container flex-column margin-bot-2 head-services">
                        <h3>Transport & Logistics</h3>
                        <p>
                            Moving something (or someone) from point A to point B? Our Gojek drivers in green jackets and helmets save your time, and energy.
                        </p>
                    </div>
                    <div class="flex-container margin-bot-4">
                        <div class="item-services">
                            <div class="icon-goride">
                                <img src={require("../../assets/images/goride_icon_new.svg")} alt="GoRide"/>
                            </div>
                            <p>Over 2 million drivers nationwide are ready to drive you safely through the traffic.</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-gocar">
                                <img src={require("../../assets/images/gocar_icon_new.svg")} alt="GoCar"/>
                            </div>
                            <p>Hundreds of thousands of drivers to drive you safely with comfort and convenience.</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-gosend">
                                <img src={require("../../assets/images/gosend_icon_new.svg")} alt="GoSend"/>
                            </div>
                            <p>Fast, reliable, and convenient delivery service for your daily needs. Order GoSend now!</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-gobox">
                                <img src={require("../../assets/images/gobox_icon_new.svg")} alt="GoBox"/>
                            </div>
                            <p>Moving or sending bulky items is now easy and convenient with GoBox.</p>
                        </div>
                    </div>

                    <div class="flex-container flex-column head-services margin-bot-2">
                        <h3>Food & FMCG</h3>
                        <p>
                            Order food from a whole lotta restaurants, get medicines delivered in a jiffy, or fill your shopping cart from many a mart.
                        </p>
                    </div>
                    <div class="flex-container margin-bot-4">
                        <div class="item-services">
                            <div class="icon-gofood">
                                <img src={require("../../assets/images/gofood_icon_new.svg")} alt="GoFood"/>
                            </div>
                            <p>The largest food delivery service in Indonesia and Southeast Asia.</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-gofoodfestival">
                                <img src={require("../../assets/images/icon-gff.svg")} alt="GoFoodFestival"/>
                            </div>
                            <p>Hundreds of thousands of drivers to drive you safely with comfort and convenience.</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-gomed">
                                <img src={require("../../assets/images/gomed_icon_new.svg")} alt="GoMed"/>
                            </div>
                            <p>Use GoMed for all your medical needs. Buy medicines, vitamins, etc. from licensed pharmacies.</p>
                        </div>
                    </div>

                    <div class="flex-container flex-column head-services margin-bot-2">
                        <h3>Payments</h3>
                        <p>
                            From split the bills to donations, we make payments reliable, easy and delightful for our customers and merchants alike.
                        </p>
                    </div>
                    <div class="flex-container margin-bot-4">
                        <div class="item-services">
                            <div class="icon-gopay">
                                <img src={require("../../assets/images/gopay_icon_new.svg")} alt="GoPay"/>
                            </div>
                            <p>Easy transaction across Gojek services and merchants.</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-gobills">
                                <img src={require("../../assets/images/gobills_icon_new.svg")} alt="GoBills"/>
                            </div>
                            <p>Bayar tagihan listrik, BPJS, gas, air, tv kabel, internet, beli token listrik. Tanpa antri dan bisa pakai GoPay, bayar tagihan apapun di GoBills, aja!</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-gopoints">
                                <img src={require("../../assets/images/gopoints_icon_new.svg")} alt="GoPoints"/>
                            </div>
                            <p>Receive a token for each transaction, swipe them to earn points, and get amazing rewards.</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-gopaylater">
                                <img src={require("../../assets/images/paylater_icon_new.svg")} alt="PayLater"/>
                            </div>
                            <p>Order any Gojek service or from any Gojek partner and pay at the end of the month with PayLater.</p>
                        </div>
                    </div>

                    <div class="flex-container flex-column head-services margin-bot-2">
                        <h3>Daily Needs</h3>
                        <p>Those regular chores that call for your attention? We have all products under daily needs to make your life simpler and hassle-free.</p>
                    </div>
                    <div class="flex-container margin-bot-4">
                        <div class="item-services">
                            <div class="icon-gomassage">
                                <img src={require("../../assets/images/gomassage_icon_new.svg")} alt="GoMassage"/>
                            </div>
                            <p>Recharge your body and experience your very own version of on demand massage!</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-goclean">
                                <img src={require("../../assets/images/goclean_icon_new.svg")} alt="GoClean"/>
                            </div>
                            <p>Prioritize what matters to you & leave all house-cleaning duties to GoClean!</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-goauto">
                                <img src={require("../../assets/images/goauto_icon_new.svg")} alt="GoAuto"/>
                            </div>
                            <p>Order GoAuto for auto care service, towing & emergency services, anytime and anywhere. All available from the GoLife app.</p>
                        </div>
                        <div class="item-services">
                            <div class="icon-goglam">
                                <img src={require("../../assets/images/goglam_icon_new.svg")} alt="GoGlam"/>
                            </div>
                            <p>With GoGlam, pamper yourself with beauty services such as mani-pedi, hair cream bath or waxing, from the comfort of your own home.</p>
                        </div>
                    </div>

                    <div class="flex-container flex-column head-services margin-bot-2">
                        <h3>News & Entertainment</h3>
                        <p>Binge on your favourite series, book tickets to the next concert, organise celebrity events, and do much more. All your treasured digital content belong here.</p>
                    </div>
                    <div class="flex-container margin-bot-4">
                        <div class="item-services">
                            <div class="icon-gotix">
                                <img src={require("../../assets/images/gotix_icon_new.svg")} alt="GoTix"/>
                            </div>
                            <p>Various exciting activities just for you. Find any tickets you want through GoTix!</p>
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