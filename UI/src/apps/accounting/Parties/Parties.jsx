import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Parties.styles';

class Parties extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Parties will mount');
  }

  componentDidMount = () => {
    console.log('Parties mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Parties will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Parties will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Parties did update');
  }

  componentWillUnmount = () => {
    console.log('Parties will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="PartiesWrapper">
        Test content
      </div>
    );
  }
}

Parties.propTypes = {
  // bla: PropTypes.string,
};

Parties.defaultProps = {
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
)(Parties);
