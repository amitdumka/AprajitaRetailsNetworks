import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './ProductSubCategory.styles';

class ProductSubCategory extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('ProductSubCategory will mount');
  }

  componentDidMount = () => {
    console.log('ProductSubCategory mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('ProductSubCategory will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('ProductSubCategory will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('ProductSubCategory did update');
  }

  componentWillUnmount = () => {
    console.log('ProductSubCategory will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="ProductSubCategoryWrapper">
        Test content
      </div>
    );
  }
}

ProductSubCategory.propTypes = {
  // bla: PropTypes.string,
};

ProductSubCategory.defaultProps = {
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
)(ProductSubCategory);
