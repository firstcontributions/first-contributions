import React from 'react';
//import Search from '../Search/Search';
import Card from './ProjectsCards';
import './CardsContainer.css';

export default class CardsContainer extends React.Component{
    
    render(){

        const projectList = [{
            
                "name":"React",
                "imageSrc":"https://camo.githubusercontent.com/22045498095171997ccf6a9554672519b9f67898/68747470733a2f2f63646e2e776f726c64766563746f726c6f676f2e636f6d2f6c6f676f732f72656163742e737667",
                "githubLink":"https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22",
                "description":"This is just an example."
            },
            {
                "name":"Exercism",
                "imageSrc":"https://avatars2.githubusercontent.com/u/5624255?v=3&s=100",
                "githubLink":"https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22",
                "description":"This is just an example"
            },{
                "name":"Fun Retros",
                "imageSrc":"https://avatars3.githubusercontent.com/u/15913975?v=3&s=100",
                "githubLink":"https://github.com/funretro/distributed/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly",
                "description":"This is just an example."
            },{
                "name":"Habitat",
                "imageSrc":"https://avatars1.githubusercontent.com/u/18171698?v=3&s=100",
                "githubLink":"https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22",
                "description":"This is just an example."
            },{
                "name":"Scikit-learn",
                "imageSrc":"https://avatars0.githubusercontent.com/u/365630?v=3&s=100",
                "githubLink":"https://github.com/scikit-learn/scikit-learn/issues?q=is%3Aopen+is%3Aissue+label%3AEasy",
                "description":"This is just an example."
            },{
                "name":"Leiningen",
                "imageSrc":"https://camo.githubusercontent.com/0f302c808c8457f6460913e33aed3478124612c2/687474703a2f2f6c65696e696e67656e2e6f72672f696d672f6c65696e696e67656e2e6a7067",
                "githubLink":"https://github.com/technomancy/leiningen/issues?q=is%3Aopen+is%3Aissue+label%3ANewbie",
                "description":"This is just an example."
            },{
                "name":"Numpy",
                "imageSrc":"https://camo.githubusercontent.com/b310fd3c9c5f7da5de0911b77d201408b76b8a58/68747470733a2f2f696d616765732e706c6f742e6c792f706c6f746c792d646f63756d656e746174696f6e2f7468756d626e61696c2f6e756d70792d6c6f676f2e6a7067",
                "githubLink":"https://github.com/numpy/numpy/issues?q=is%3Aopen+is%3Aissue+label%3A%22Easy+Fix%22",
                "description":"This is just an example."
            },{
                "name":"Elasticsearch",
                "imageSrc":"https://avatars2.githubusercontent.com/u/6764390?v=3&s=100",
                "githubLink":"https://github.com/elastic/elasticsearch/issues?q=is%3Aopen+is%3Aissue+label%3A%22low+hanging+fruit%22",
                "description":"This is just an example."
            },{
                "name":"Homebrew",
                "imageSrc":"https://avatars2.githubusercontent.com/u/1503512?v=3&s=100",
                "githubLink":"https://github.com/Homebrew/brew/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22",
                "description":"This is just an example."
            },{
                "name":"Rust",
                "imageSrc":"https://avatars1.githubusercontent.com/u/5430905?v=3&s=100",
                "githubLink":"https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy",
                "description":"This is just an example."
            },{
                "name":"Vuejs",
                "imageSrc":"https://avatars1.githubusercontent.com/u/6128107?v=3&s=100",
                "githubLink":"https://github.com/vuejs/vue/issues?q=is%3Aopen+is%3Aissue+label%3A%22contribution+welcome%22",
                "description":"This is just an example."
            },{
                "name":"Suave",
                "imageSrc":"https://avatars2.githubusercontent.com/u/5822862?v=3&s=100",
                "githubLink":"https://github.com/SuaveIO/suave/issues?q=is%3Aopen+is%3Aissue+label%3Ahardness-easy",
                "description":"This is just an example."
            },{
                "name":"OpenRA",
                "imageSrc":"https://avatars3.githubusercontent.com/u/409046?v=3&s=100",
                "githubLink":"https://github.com/OpenRA/OpenRA/issues?q=is%3Aopen+is%3Aissue+label%3AEasy",
                "description":"This is just an example."
            },{
                "name":"PowerShell",
                "imageSrc":"https://avatars0.githubusercontent.com/u/11524380?v=3&s=100",
                "githubLink":"https://github.com/powershell/powershell/issues?q=is%3Aopen+is%3Aissue+label%3AUp-for-Grabs",
                "description":"This is just an example."
            },{
                "name":"Coala",
                "imageSrc":"https://avatars2.githubusercontent.com/u/10620750?v=3&s=100",
                "githubLink":"https://github.com/coala/coala/issues?q=is%3Aopen+is%3Aissue+label%3Adifficulty%2Flow+label%3Adifficulty%2Fnewcomer",
                "description":"This is just an example."
            },{
                "name":"Moment",
                "imageSrc":"https://avatars2.githubusercontent.com/u/4129662?v=3&s=100",
                "githubLink":"https://github.com/moment/moment/issues?q=is%3Aopen+is%3Aissue+label%3AUp-For-Grabs",
                "description":"This is just an example."
            },{
                "name":"AVA",
                "imageSrc":"https://avatars0.githubusercontent.com/u/8527916?v=3&s=100",
                "githubLink":"https://github.com/avajs/ava/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+for+beginner%22",
                "description":"This is just an example."
            },{
                "name":"freeCodeCamp",
                "imageSrc":"https://avatars0.githubusercontent.com/u/9892522?v=3&s=100",
                "githubLink":"https://github.com/freeCodeCamp/freeCodeCamp/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only",
                "description":"This is just an example."
            },{
                "name":"Webpack",
                "imageSrc":"https://avatars3.githubusercontent.com/u/2105791?v=3&s=100",
                "githubLink":"https://github.com/webpack/webpack/issues?q=is%3Aopen+is%3Aissue+label%3A%22D1%3A+Easy+%28Contrib.+Difficulty%29%22",
                "description":"This is just an example."
            },{
                "name":"Hoodie",
                "imageSrc":"https://avatars1.githubusercontent.com/u/1888826?v=3&s=100",
                "githubLink":"https://github.com/hoodiehq/hoodie/issues?q=is%3Aopen+is%3Aissue+label%3Afirst-timers-only",
                "description":"This is just an example."
            },{
                "name":"Pouchdb",
                "imageSrc":"https://avatars3.githubusercontent.com/u/3406112?v=3&s=100",
                "githubLink":"https://github.com/pouchdb/pouchdb/issues?q=is%3Aopen+is%3Aissue+label%3A%22first+timers+only%22",
                "description":"This is just an example."
            },{
                "name":"Neovim",
                "imageSrc":"https://avatars0.githubusercontent.com/u/6471485?v=3&s=100",
                "githubLink":"https://github.com/neovim/neovim/issues?q=is%3Aopen+is%3Aissue+label%3Aentry-level",
                "description":"This is just an example."
            },{
                "name":"Babel",
                "imageSrc":"https://avatars2.githubusercontent.com/u/9637642?v=3&s=100",
                "githubLink":"https://github.com/babel/babel/issues?q=is%3Aopen+is%3Aissue+label%3Abeginner-friendly",
                "description":"This is just an example."
            },{
                "name":"Brackets",
                "imageSrc":"https://github.com/adobe/brackets/raw/gh-pages/images/brackets_128.png?raw=true",
                "githubLink":"https://github.com/adobe/brackets/labels/Starter%20bug",
                "description":"This is just an example."
            },{
                "name":"Node.js",
                "imageSrc":"https://avatars1.githubusercontent.com/u/9950313?v=3&s=100",
                "githubLink":"https://github.com/nodejs/node/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22",
                "description":"This is just an example."
            },{
                "name":"Semantic-UI-React",
                "imageSrc":"https://github.com/Semantic-Org/Semantic-UI-React/raw/master/docs/app/logo.png",
                "githubLink":"https://github.com/Semantic-Org/Semantic-UI-React/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+contribution%22",
                "description":"This is just an example."
            }

        ]

        return(
            <div className="Container-layout">
                {projectList.map((item) => {
                    return(
                        <Card name={item.name} logoLink={item.imageSrc} githubLink={item.githubLink} description={item.description}/>
                    )
                })}
                
            </div>
        )
    }

}