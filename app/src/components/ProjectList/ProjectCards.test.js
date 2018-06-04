import React from 'react';
import renderer from 'react-test-renderer';
import Card from './ProjectsCards';

it('renders a project card', () => {
  const tree = renderer.create(
    <Card
              name='Awesome Project'
              logoLink='http://awesome-project.com/logo.jpg'
              githubLink='https://github.com/awesome-project'
              description='Simply awesome Project'
    />
  ).toJSON();
  expect(tree).toMatchSnapshot();
});

