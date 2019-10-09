import React, { Component } from 'react'

class FooterNavigation extends Component {
    render() {
        return (
            <footer>
                <div class="flex-container margin-bot-4">
                    <div class="logo-white">
                        <img src={require('../../assets/images/gojek-white-text.svg')} alt="Super App"/>
                    </div>
                    <div class="item-footer">
                        <h3>About Gojek</h3>
                        <ul>
                            <li><a href="#">Media Centre</a></li>
                            <li><a href="#">About Us</a></li>
                            <li><a href="#">Careers</a></li>
                            <li><a href="#">Blog</a></li>
                        </ul>
                    </div>
                    <div class="item-footer">
                        <h3>Support</h3>
                        <ul>
                            <li><a href="#">Contact Us</a></li>
                            <li><a href="#">Privacy Policy</a></li>
                            <li><a href="#">Terms & Conditions</a></li>
                            <li><a href="#">Help Centre</a></li>
                        </ul>
                    </div>
                    <div class="item-footer">
                        <h3>Follow Us On</h3>
                        <ul>
                            <li><a href="#">Facebook</a></li>
                            <li><a href="#">Twitter</a></li>
                            <li><a href="#">Instagram</a></li>
                            <li><a href="#">Youtube</a></li>
                        </ul>
                    </div>
                    <div class="item-footer">
                        <h3>Download</h3>
                        <a href="#"><img src={require('../../assets/images/playstore.jpg')} alt="Download Playstore"/></a>
                        <a href="#"><img src={require('../../assets/images/appstore.jpg')} alt="Download Appstore"/></a>
                    </div>
                </div>
                <div class="flex-container">
                    <div class="item-footer">
                        <h3>Transport & Logistics</h3>
                        <ul>
                            <li><a href="#">GoRide</a></li>
                            <li><a href="#">GoCar</a></li>
                            <li><a href="#">GoSend</a></li>
                            <li><a href="#">GoBox</a></li>
                        </ul>
                    </div>
                    <div class="item-footer">
                        <h3>Food & FMCG</h3>
                        <ul>
                            <li><a href="#">GoFood</a></li>
                            <li><a href="#">GoFood Festival</a></li>
                            <li><a href="#">GoMed</a></li>
                        </ul>
                    </div>
                    <div class="item-footer">
                        <h3>Payments</h3>
                        <ul>
                            <li><a href="#">GoPay</a></li>
                            <li><a href="#">GoBills</a></li>
                            <li><a href="#">GoPoint</a></li>
                            <li><a href="#">PayLater</a></li>
                            <li><a href="#">GoPulsa</a></li>
                        </ul>
                    </div>
                    <div class="item-footer">
                        <h3>Daily Needs</h3>
                        <ul>
                            <li><a href="#">GoMassage</a></li>
                            <li><a href="#">GoClean</a></li>
                            <li><a href="#">GoAuto</a></li>
                            <li><a href="#">GoGlam</a></li>
                            <li><a href="#">GoLaundry</a></li>
                            <li><a href="#">GoDaily</a></li>
                            <li><a href="#">GoFix</a></li>
                        </ul>
                    </div>
                    <div class="item-footer">
                        <h3>News & Entertainment</h3>
                        <ul>
                            <li><a href="#">GoTix</a></li>
                        </ul>
                    </div>
                </div>
                <div class="container-fluid">
                    <div class="container">
                        <hr/>
                    </div>
                </div>
                <div class="flex-container flex-column flex-center margin-bot-2">
                    <div class="copyright">
                        <p>© 2019 Gojek</p>
                    </div>
                    <div class="copyright">
                        <p>Gojek is a trademark of PT Aplikasi Karya Anak Bangsa. Registered in the Directorate General of Intellectual Property of the Republic of Indonesia.</p>
                    </div>
                </div>
            </footer>
        )
    }
}

export default FooterNavigation