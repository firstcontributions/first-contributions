import React from 'react';
import renderer from 'react-test-renderer';
import TwitterCard from './Twitter';

it('renders a project card', () => {
  const tree = renderer.create(
    <TwitterCard/>
  ).toJSON();
  expect(tree).toMatchSnapshot();
});

