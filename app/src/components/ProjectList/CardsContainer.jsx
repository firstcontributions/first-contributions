import React from 'react';
import Card from '../ProjectList/ProjectsCards';
import './CardsContainer.css';

export default class CardsContainer extends React.Component{

    render(){
        const projectList = [{
            
                "name":"React",
                "logo":"https://camo.githubusercontent.com/22045498095171997ccf6a9554672519b9f67898/68747470733a2f2f63646e2e776f726c64766563746f726c6f676f2e636f6d2f6c6f676f732f72656163742e737667",
                "imageSrc":"https://github.com/facebook/react/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+bug%22",
                "description":"This is just an example."
            },
            {
                "name":"Exercism",
                "logo":"https://avatars2.githubusercontent.com/u/5624255?v=3&s=100",
                "imageSrc":"https://github.com/exercism/exercism.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+patch%22",
                "description":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed congue felis id lacinia aliquam. Sed condimentum, erat sed pulvinar pretium, dolor leo efficitur nisi, eget faucibus turpis nisi nec justo. Sed sagittis mattis nibh et scelerisque. Vestibulum congue eleifend justo. Fusce efficitur sem eu sagittis bibendum. Pellentesque dictum turpis id nisi commodo, quis dapibus leo iaculis. Aliquam vel felis ipsum. In vel tellus et ligula hendrerit consequat nec id libero. Phasellus tempor felis vitae tincidunt facilisis. Praesent non massa finibus urna porta condimentum. Maecenas blandit mi et elementum venenatis. Pellentesque non tellus ex."
            }
        ]

        return(
            <div className="Container-layout">
                <Card name={projectList[1].name} logo={projectList[1].logo} link={projectList[1].imageSrc} description={projectList[1].description}/>
                <Card name={projectList[1].name} logo={projectList[1].logo} link={projectList[1].imageSrc} description={projectList[1].description}/>
                <Card name={projectList[1].name} logo={projectList[1].logo} link={projectList[1].imageSrc} description={projectList[1].description}/>
                <Card name={projectList[1].name} logo={projectList[1].logo} link={projectList[1].imageSrc} description={projectList[1].description}/>
                <Card name={projectList[1].name} logo={projectList[1].logo} link={projectList[1].imageSrc} description={projectList[1].description}/>
                <Card name={projectList[0].name} logo={projectList[0].logo} link={projectList[0].imageSrc} description={projectList[0].description}/>
                <Card name={projectList[0].name} logo={projectList[0].logo} link={projectList[0].imageSrc} description={projectList[0].description}/>
                <Card name={projectList[0].name} logo={projectList[0].logo} link={projectList[0].imageSrc} description={projectList[0].description}/>
                <Card name={projectList[0].name} logo={projectList[0].logo} link={projectList[0].imageSrc} description={projectList[0].description}/>
                <Card name={projectList[0].name} logo={projectList[0].logo} link={projectList[0].imageSrc} description={projectList[0].description}/>
                <Card name={projectList[0].name} logo={projectList[0].logo} link={projectList[0].imageSrc} description={projectList[0].description}/>
            </div>
        )
    }

}