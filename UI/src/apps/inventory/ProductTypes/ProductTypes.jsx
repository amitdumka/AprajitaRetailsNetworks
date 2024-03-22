import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './ProductTypes.styles';

class ProductTypes extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('ProductTypes will mount');
  }

  componentDidMount = () => {
    console.log('ProductTypes mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('ProductTypes will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('ProductTypes will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('ProductTypes did update');
  }

  componentWillUnmount = () => {
    console.log('ProductTypes will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="ProductTypesWrapper">
        Test content
      </div>
    );
  }
}

ProductTypes.propTypes = {
  // bla: PropTypes.string,
};

ProductTypes.defaultProps = {
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
)(ProductTypes);
