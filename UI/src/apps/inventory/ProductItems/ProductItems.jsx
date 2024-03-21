import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './ProductItems.styles';

class ProductItems extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('ProductItems will mount');
  }

  componentDidMount = () => {
    console.log('ProductItems mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('ProductItems will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('ProductItems will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('ProductItems did update');
  }

  componentWillUnmount = () => {
    console.log('ProductItems will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="ProductItemsWrapper">
        Test content
      </div>
    );
  }
}

ProductItems.propTypes = {
  // bla: PropTypes.string,
};

ProductItems.defaultProps = {
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
)(ProductItems);
