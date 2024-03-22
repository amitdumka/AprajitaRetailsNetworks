import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Brands.styles';

class Brands extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Brands will mount');
  }

  componentDidMount = () => {
    console.log('Brands mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Brands will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Brands will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Brands did update');
  }

  componentWillUnmount = () => {
    console.log('Brands will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="BrandsWrapper">
        Test content
      </div>
    );
  }
}

Brands.propTypes = {
  // bla: PropTypes.string,
};

Brands.defaultProps = {
  // bla: 'test',
};

const mapStateToProps = state => ({
  // blabla: state.blabla,
});

const mapDispatchToProps = dispatch => ({
  // fnBlaBla: () => dispatch(action.name()),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Brands);
