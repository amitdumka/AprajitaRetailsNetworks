import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './PoductCategory.styles';

class PoductCategory extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('PoductCategory will mount');
  }

  componentDidMount = () => {
    console.log('PoductCategory mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('PoductCategory will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('PoductCategory will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('PoductCategory did update');
  }

  componentWillUnmount = () => {
    console.log('PoductCategory will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="PoductCategoryWrapper">
        Test content
      </div>
    );
  }
}

PoductCategory.propTypes = {
  // bla: PropTypes.string,
};

PoductCategory.defaultProps = {
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
)(PoductCategory);
